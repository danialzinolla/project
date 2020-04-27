import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';

import { Koment} from './koment';


@Injectable({ providedIn: 'root' })
export class KomentService {

  BASE_URL = 'http://127.0.0.1:8000';

  // private heroesUrl = 'api/heroes';  // URL to web api

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient) { }

  // getKoments(): Observable<Koment[]> {
  //   return this.http.get<Koment[]>(`${this.BASE_URL}/ani/koments/`);
  //
  // }

  getKomentsByAnime(id): Observable<Koment[]> {
    return this.http.get<Koment[]>(`${this.BASE_URL}/ani/animes/${id}/koments/`);
  }

  // getKoment(id): Observable<Koment> {
  //   return this.http.get<Koment>(`${this.BASE_URL}/ani/koments/${id}/`);
  // }




}
