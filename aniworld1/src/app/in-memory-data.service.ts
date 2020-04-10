import { InMemoryDbService } from 'angular-in-memory-web-api';
import { Hero } from './hero';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class InMemoryDataService implements InMemoryDbService {
  createDb() {
    const heroes = [
      { id: 1, name: 'Shaman King', image: "https://dere.shikimori.one/system/animes/original/154.jpg?1561452772",  url:"https://anistar.org/"},
      { id: 2, name: 'Gintama' , image: "https://cdn.animenewsnetwork.com/thumbnails/max450x450/cms/news.2/144127/gintama-event-visual.jpg",  url:"https://anistar.org/"},
      { id: 3, name: 'Bleach' , image: "https://vignette.wikia.nocookie.net/anime-characters-fight/images/e/ee/Bleach_last.jpg/revision/latest/scale-to-width-down/340?cb=20160125202254&path-prefix=ru",  url:"https://anistar.org/"},
      { id: 4, name: 'Demon slayer', image: "https://st.kp.yandex.net/images/film_iphone/iphone360_1220920.jpg" ,  url:"https://anistar.org/"},
      { id: 5, name: 'Danmachi', image: "https://69.media.tumblr.com/af9c202d86bfcd2d84c8e95f003d4761/tumblr_pspyrkuV2w1rzp45wo1_1280.jpg" ,  url:"https://anistar.org/"},
      { id: 6, name: 'My hero academia' , image: "https://kinogo.zone/uploads/posts/2020-01/1578409170-1675396412-moya-geroyskaya-akademiya-film-2-geroi-vosstanut.jpg",  url:"https://anistar.org/"},
      { id: 7, name: 'Haikyuu', image: "https://wakamedia.wakanim.tv/library-400/81_637140861467151490Haikyu_S4_Small_RU_hq.jpg" ,  url:"https://anistar.org/"},
      { id: 8, name: 'No life no game' , image: "https://i1.wp.com/manga-home.com/wp-content/uploads/2017/03/No-Game-No-Life.jpg?fit=491%2C650&ssl=1",  url:"https://anistar.org/"},
      { id: 9, name: 'Kuroko no Basuke' , image: "https://i.ebayimg.com/images/g/Ej8AAOSwqZFeTHmN/s-l640.jpg",  url:"https://anistar.org/"},
      { id: 10, name: 'Tower of God', image: "https://static.findanime.org/uploads/pics/01/08/058.jpg" ,  url:"https://anistar.org/"},
      { id: 11, name: 'Dr Stone', image: "https://lh3.googleusercontent.com/proxy/XAA32H6kFX3c5196RVNS8PuGnYf3sW1rYE4VNK7sJv1Upfm6zbiWq15iyo7mvDWWmKP-SP4uPozN50BXr-uB_lTL-85hSAYOufCpqKboJbFuNtZSBmHip8uDRvpQ7jXsiNh1vR1OOYzjuXg7bI0sJv97GjmTlg" ,  url:"https://anistar.org/"},
      { id: 12, name: 'Naruto' , image: "https://lh3.googleusercontent.com/proxy/SZkNXgNzHSZgBRVvtIYmSx49ssxXxDaX3P24SQFS3eM4AWMyfNIjk8t3TBFJsEt2a37GoCFC_g_1GLkwVIvPFr4",  url:"https://anistar.org/"},
      { id: 13, name: 'One Piece' , image: "https://dere.shikimori.one/system/animes/original/154.jpg?1561452772",  url:"https://anistar.org/"},
      { id: 14, name: 'Mob Psycho' , image: "https://upload.wikimedia.org/wikipedia/ru/4/4e/Mob_Psycho_100.png",  url:"https://anistar.org/"},
      { id: 15, name: 'High School DxD' , image: "https://vignette.wikia.nocookie.net/highschooldxd/images/e/ec/Cover_of_True_Light_Novel_Volume_1.jpg/revision/latest?cb=20191019192721&path-prefix=ru",  url:"https://anistar.org/"},
      { id: 16, name: 'Plunderer', image: "https://vignette.wikia.nocookie.net/plunderer/images/f/fd/PlundererVisual3.jpg/revision/latest/top-crop/width/360/height/450?cb=20200317033557" ,  url:"https://anistar.org/"},
      { id: 17, name: 'Shoumetsu Toshi', image: "https://vignette.wikia.nocookie.net/anime/images/4/4b/1554228487.jpg/revision/latest?cb=20190415081426&path-prefix=ru", url:"https://anistar.org/"},
      { id: 18, name: 'One punch man' , image: "https://www.toramp.com/posters/shows/1816/width360/onepunch_man.jpg", url:"https://anistar.org/"},
      { id: 19, name: 'Toradora' , image: "https://film-like.com/images/film/full/1f/61914.jpg", url:"https://anistar.org/"},
      { id: 20, name: 'SAO' , image: "https://vignette.wikia.nocookie.net/sword-art-online/images/7/71/SAO_%281_%D0%BF%D0%BE%D1%81%D1%82%D0%B5%D1%80%29.jpg/revision/latest/scale-to-width-down/340?cb=20131231155909&path-prefix=ru",url:"https://anistar.org/"}
    ];
    return {heroes};
  }

  // Overrides the genId method to ensure that a hero always has an id.
  // If the heroes array is empty,
  // the method below returns the initial number (11).
  // if the heroes array is not empty, the method below returns the highest
  // hero id + 1.
  genId(heroes: Hero[]): number {
    return heroes.length > 0 ? Math.max(...heroes.map(hero => hero.id)) + 1 : 11;
  }
}
