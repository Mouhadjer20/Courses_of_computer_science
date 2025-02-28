import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ToDo } from '../Models/to-do';

@Injectable({
  providedIn: 'root'
})
export class ToDoService {
  private apiUrl = "http://localhost:3000/todos";
  constructor(private httpClient: HttpClient) { }

  // Get All To Do
  getAllToDo() : Observable<ToDo[]>
  {
    return this.httpClient.get<ToDo[]>(this.apiUrl);
  }

  // Post To Do
  createToDo(newTodo: ToDo) : Observable<ToDo>
  {
    return this.httpClient.post<ToDo>(this.apiUrl, JSON.stringify(newTodo));
  }

  // Get To Do By Id
  getToDoById(idToDo: number) : Observable<ToDo>
  {
    return this.httpClient.get<ToDo>(`${this.apiUrl}/${idToDo}`);
  }

  // Update To Do
  updateToDo(updatedTodo: ToDo) : Observable<ToDo>
  {
    return this.httpClient.put<ToDo>(`${this.apiUrl}/${updatedTodo.id}`, JSON.stringify(updatedTodo));
  }

  // Deleted To Do
  deleteToDo(idToDo: number) : Observable<void>
  {
    return this.httpClient.delete<void>(`${this.apiUrl}/${idToDo}`);
  }
}
