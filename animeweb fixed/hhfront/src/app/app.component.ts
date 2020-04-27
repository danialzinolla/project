import { Component } from '@angular/core';
import {HeroService} from './hero.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'AniWorld';


  logged = false;

  username = '';
  password = '';

  constructor(private heroService: HeroService) {}

  // tslint:disable-next-line:use-lifecycle-interface
  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }

  login() {
    this.heroService.login(this.username, this.password)
        .subscribe(res => {

          localStorage.setItem('token', res.token);

          this.logged = true;

          this.username = '';
          this.password = '';
        });
  }

  logout() {
    localStorage.clear();
    this.logged = false;
  }
}

