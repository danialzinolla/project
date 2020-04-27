import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

import { Hero, LoginResponse} from './hero';


@Injectable({ providedIn: 'root' })
export class HeroService {

  BASE_URL = 'http://127.0.0.1:8000';

  // private heroesUrl = 'api/heroes';  // URL to web api

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient) { }

  /** GET heroes from the server */
  getHeroes(): Observable<Hero[]> {
    return this.http.get<Hero[]>(`${this.BASE_URL}/ani/animes/`);

  }

  /** GET hero by id. Return `undefined` when id not found */
  getHero(id): Observable<Hero> {
    return this.http.get<Hero>(`${this.BASE_URL}/ani/animes/${id}/`);
  }



  /* GET heroes whose name contains search term */
  searchHeroes(term: string): Observable<Hero[]> {
    if (!term.trim()) {
      // if not search term, return empty hero array.
      return of([]);
    }
    return this.http.get<Hero[]>(`${this.BASE_URL}/?name=${term}`).pipe();
  }

  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.BASE_URL}/ani/login/`, {
      username,
      password
    });
  }

}
