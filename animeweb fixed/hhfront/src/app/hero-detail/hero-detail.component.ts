import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { Hero } from '../hero';
import { HeroService } from '../hero.service';

import {Koment} from '../koment';
import {KomentService} from '../koment.service';

import {Simianime} from '../semiani';
import {SemianiService} from '../semiani.service';

import {AnimeWeb} from '../aniweb';
import {AniwebService} from '../aniweb.service';

@Component({
  selector: 'app-hero-detail',
  templateUrl: './hero-detail.component.html',
  styleUrls: [ './hero-detail.component.css' ]
})
export class HeroDetailComponent implements OnInit {
  hero: Hero;
  koments: Koment[] = [];
  similars: Simianime[] = [];
  webs: AnimeWeb[] = [];


  constructor(
    private route: ActivatedRoute,
    private heroService: HeroService,
    private komentService: KomentService,
    private semianiService: SemianiService,
    private animewebService: AniwebService,
    private location: Location
  ) {}

  ngOnInit(): void {
    this.getHero();
    this.getKoments();
    this.getSimilars();
    this.getWebs();
  }

  getHero(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.heroService.getHero(id)
      .subscribe(hero => this.hero = hero);
  }

  getKoments() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.komentService.getKomentsByAnime(id).subscribe(koments => this.koments = koments);
  }

  getSimilars() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.semianiService.getSimilarsByAnime(id).subscribe(similars => this.similars = similars);
  }

  getWebs() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.animewebService.getWebsByAnime(id).subscribe(webs => this.webs = webs);
  }

  goBack(): void {
    this.location.back();
  }


}
