import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ToDoComponent } from './Components/to-do/to-do.component';
import { AboutusComponent } from './Components/aboutus/aboutus.component';
import { ContactusComponent } from './Components/contactus/contactus.component';
import { FooterComponent } from './Components/footer/footer.component';
import { HeaderComponent } from './Components/header/header.component';
import { HomeComponent } from './Components/home/home.component';
import { TodoDetailsComponent } from './Components/todo-details/todo-details.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { NotFoundComponent } from './Components/not-found/not-found.component';

@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet,
    ToDoComponent,
    FontAwesomeModule,
    AboutusComponent,
    ContactusComponent,
    FooterComponent,
    HeaderComponent,
    HomeComponent,
    TodoDetailsComponent,
    NotFoundComponent
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent {
  title = 'To-Do-List';
}
