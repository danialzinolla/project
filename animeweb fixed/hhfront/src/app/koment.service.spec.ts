import { TestBed } from '@angular/core/testing';

import { KomentService } from './koment.service';

describe('KomentService', () => {
  let service: KomentService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(KomentService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
