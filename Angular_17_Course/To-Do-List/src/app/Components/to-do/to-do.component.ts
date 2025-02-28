import { Component, OnInit, input } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { ToDo } from "../../Models/to-do";
import { ToDoService } from "../../services/to-do.service";
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-to-do',
  imports: [
    FontAwesomeModule,
    FormsModule,
    CommonModule,
    RouterModule
  ],
  templateUrl: './to-do.component.html',
  styleUrl: './to-do.component.css'
})

export class ToDoComponent implements OnInit{
  Title:string = "To Do Application"
  ImageLink:string = "https://www.gstatic.com/images/branding/product/1x/docs_2020q4_48dp.png"

  toDos : ToDo[] = [];
  newToDo : ToDo = {} as ToDo;

  constructor(private todoService: ToDoService) {}

  ngOnInit(): void {
    this.getToDos()
  }

  getToDos(): void
  {
    this.todoService.getAllToDo().subscribe(toDos => {
      this.toDos = toDos;
    });
  }

  createToDo(): void
  {
    console.log(this.toDos);
    const idGenerate = Number(this.toDos.reduce((max, task) => task.id > max ? task.id : max, 0)) + 1;
    const newToDo = {
      id: idGenerate,
      title: this.newToDo.title,
      description: `${this.newToDo.title} number ${idGenerate}`,
      completed: false
    };
    this.newToDo = newToDo
    this.todoService.createToDo(this.newToDo).subscribe(todo =>{
      this.toDos.push(todo);
    });
  }

  deleteToDo(toDoId: number): void
  {
    this.todoService.deleteToDo(toDoId).subscribe(()=>{
      this.toDos = this.toDos.filter(todo => todo.id !== toDoId);
    })
  }
}