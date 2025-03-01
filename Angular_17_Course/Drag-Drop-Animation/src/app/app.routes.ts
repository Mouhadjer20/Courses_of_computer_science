import { Routes } from '@angular/router';
import { TodoComponent } from './Components/todo/todo.component';
import { NotFoundComponent } from './Components/not-found/not-found.component';

export const routes: Routes = [
    {path: "", redirectTo: "/todo", pathMatch: "full"},
    {path: "todo", component:TodoComponent, title: "Todo"},
    {path: "**", component:NotFoundComponent, title: "404 Not Found"}
];


