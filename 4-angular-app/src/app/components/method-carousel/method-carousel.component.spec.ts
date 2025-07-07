import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MethodCarouselComponent } from './method-carousel.component';

describe('MethodCarouselComponent', () => {
  let component: MethodCarouselComponent;
  let fixture: ComponentFixture<MethodCarouselComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MethodCarouselComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MethodCarouselComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
