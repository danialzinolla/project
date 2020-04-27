import { TestBed } from '@angular/core/testing';

import { SemianiService } from './semiani.service';

describe('SemianiService', () => {
  let service: SemianiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SemianiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
