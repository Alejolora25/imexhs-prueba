import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AreaResultTableComponent } from './area-result-table.component';

describe('AreaResultTableComponent', () => {
  let component: AreaResultTableComponent;
  let fixture: ComponentFixture<AreaResultTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AreaResultTableComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AreaResultTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
