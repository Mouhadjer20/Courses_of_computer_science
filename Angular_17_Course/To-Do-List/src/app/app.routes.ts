import { Routes } from '@angular/router';
import { HomeComponent } from './Components/home/home.component';
import { AboutusComponent } from './Components/aboutus/aboutus.component';
import { ContactusComponent } from './Components/contactus/contactus.component';
import { TodoDetailsComponent } from './Components/todo-details/todo-details.component';
import { NotFoundComponent } from './Components/not-found/not-found.component';
import { ToDoComponent } from './Components/to-do/to-do.component';

export const routes: Routes = [
    {path: '', redirectTo: '/home', pathMatch: 'full'},
    {path: 'home', component: HomeComponent, title: 'Home Page'},
    {path: 'todos', component: ToDoComponent, title: 'ToDo Page'},
    {path: 'aboutus', component: AboutusComponent, title: 'ABout Us Page'},
    {path: 'contactus', component: ContactusComponent, title: 'Contact Us Page'},
    {path: 'todos/:id', component: TodoDetailsComponent, title: 'Todo Details Page'},
    {path: '**', component: NotFoundComponent, title: '404 Not Found'}
];
