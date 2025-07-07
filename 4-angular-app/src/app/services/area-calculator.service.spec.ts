import { TestBed } from '@angular/core/testing';

import { AreaCalculatorService } from './area-calculator.service';

describe('AreaCalculatorService', () => {
  let service: AreaCalculatorService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AreaCalculatorService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
