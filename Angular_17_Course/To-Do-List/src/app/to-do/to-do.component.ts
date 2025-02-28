import { Component, input } from '@angular/core';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

@Component({
  selector: 'app-to-do',
  imports: [FontAwesomeModule],
  templateUrl: './to-do.component.html',
  styleUrl: './to-do.component.css'
})
export class ToDoComponent {
  Title:string = "To Do Application"
  ImageLink:string = "https://www.gstatic.com/images/branding/product/1x/docs_2020q4_48dp.png"

  tasks : string[] = [];
  newTask : string = "";

  addTask(){
    if(this.newTask !== ""){
      this.tasks.push(this.newTask)
    }
  }
}