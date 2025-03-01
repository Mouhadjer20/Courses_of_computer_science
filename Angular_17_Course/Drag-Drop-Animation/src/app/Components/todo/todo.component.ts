import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatIconModule} from '@angular/material/icon';
import {MatInputModule} from '@angular/material/input';
import { Task } from "../../Models/task";
import {
  CdkDragDrop,
  moveItemInArray,
  transferArrayItem,
  CdkDrag,
  CdkDropList,
} from '@angular/cdk/drag-drop';

@Component({
  selector: 'app-todo',
  imports: [
    MatCardModule,
    MatFormFieldModule,
    MatIconModule,
    MatInputModule,
    ReactiveFormsModule,
    CdkDropList,
    CdkDrag
  ],
  templateUrl: './todo.component.html',
  styleUrl: './todo.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class TodoComponent implements OnInit {
  todoForm!: FormGroup;
  tasks: Task[] = [];
  inprogress: Task[] = [];
  done: Task[] = [];
  isEditing: boolean = false;
  updatedIndex!: any;

  constructor(private fb:FormBuilder) {}

  ngOnInit(): void {
    this.todoForm = this.fb.group({
      item: ['', Validators.required]
    })
  }

  addTask(){
    this.tasks.push({
      title: this.todoForm.value.item,
      completed: false
    });
    this.todoForm.reset();
  }

  updateTask(){
    this.tasks[this.updatedIndex].title = this.todoForm.value.item
    this.tasks[this.updatedIndex].completed = false;
    this.todoForm.reset();
    this.updatedIndex = undefined;
    this.isEditing = false;
  }

  deleteTask(taskIndex: number){
    this.tasks.splice(taskIndex, 1);
    this.todoForm.reset();
  }

  deleteTaskInProgress(taskIndex: number){
    this.inprogress.splice(taskIndex, 1);
    this.todoForm.reset();
  }

  deleteDoneTask(taskIndex: number){
    this.done.splice(taskIndex, 1);
    this.todoForm.reset();
  }

  onEditTask(newTask:Task, taskIndex: number){
    this.todoForm.controls['item'].setValue(newTask.title);
    this.updatedIndex = taskIndex;
    this.isEditing = true;

  }
  drop(event: CdkDragDrop<Task[]>) {
    if (event.previousContainer === event.container) {
      moveItemInArray(event.container.data, event.previousIndex, event.currentIndex);
    } else {
      transferArrayItem(
        event.previousContainer.data,
        event.container.data,
        event.previousIndex,
        event.currentIndex,
      );
    }
  }
}
