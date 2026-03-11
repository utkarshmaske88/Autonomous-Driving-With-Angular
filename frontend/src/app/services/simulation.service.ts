import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SimulationService {

  constructor(private http: HttpClient) {}

  getSimulation(): Observable<any> {

    return this.http.get('http://localhost:8000/simulate');

  }
}