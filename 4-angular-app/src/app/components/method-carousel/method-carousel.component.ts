import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { MatStepperModule } from '@angular/material/stepper';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-method-carousel',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatStepperModule, MatButtonModule],
  templateUrl: './method-carousel.component.html',
  styleUrl: './method-carousel.component.scss'
})
export class MethodCarouselComponent {

}
