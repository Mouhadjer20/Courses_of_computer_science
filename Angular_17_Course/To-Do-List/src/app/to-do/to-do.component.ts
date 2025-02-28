import { Component, input } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { take } from 'rxjs';

@Component({
  selector: 'app-to-do',
  imports: [
    FontAwesomeModule,
    FormsModule
  ],
  templateUrl: './to-do.component.html',
  styleUrl: './to-do.component.css'
})
export class ToDoComponent {
  Title:string = "To Do Application"
  ImageLink:string = "https://www.gstatic.com/images/branding/product/1x/docs_2020q4_48dp.png"

  tasks : string[] = [];
  newTask : string = "";
  isAvailibale: boolean = false;

  addTask(){
    if (this.newTask.trim()) {
      this.isAvailibale = true;
      this.tasks.push(this.newTask.trim());
      this.newTask = "";
    }
  }

  removeTask(idxTask: number) {
    this.tasks.splice(idxTask, 1);
    if (this.tasks.length < 1)
      this.isAvailibale = false;
  }

  editTask(idxTask: number, newTask: string) : string | void{
    if (idxTask >= 0 && idxTask < this.tasks.length){
      let trimmedTask = newTask.trim();
      
      if (trimmedTask !== "") { // Prevent empty or unchanged value
        if(trimmedTask !== this.tasks[idxTask])
        this.tasks[idxTask] = trimmedTask;
      }else{
        alert("Put new Value in input of new task after that click in edit")
      }
    }
  }
}