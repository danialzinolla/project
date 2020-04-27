import { TestBed } from '@angular/core/testing';

import { AniwebService } from './aniweb.service';

describe('AniwebService', () => {
  let service: AniwebService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AniwebService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
