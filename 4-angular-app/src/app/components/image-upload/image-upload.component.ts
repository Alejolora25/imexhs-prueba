import { Component, ViewChild, ElementRef, signal } from '@angular/core';
import { MatSliderModule } from '@angular/material/slider';
import { MatButtonModule } from '@angular/material/button';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AreaResultService } from '../../services/area-result.service';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatCardModule } from '@angular/material/card';


@Component({
  selector: 'app-image-upload',
  standalone: true,
  imports: [CommonModule, FormsModule, MatSliderModule, MatButtonModule,
    MatProgressSpinnerModule, MatCardModule],
  templateUrl: './image-upload.component.html',
  styleUrl: './image-upload.component.scss'
})


export class ImageUploadComponent {
  constructor(private areaService: AreaResultService) {}

  @ViewChild('canvas', { static: false }) canvasRef!: ElementRef<HTMLCanvasElement>;
  @ViewChild('fileInput', { static: false }) fileInputRef!: ElementRef<HTMLInputElement>;

  imageLoaded = signal(false);
  imageWidth = 0;
  imageHeight = 0;
  numPoints = 1000; // valor por defecto
  readonly minPoints = 100;
  readonly maxPoints = 10000;
  readonly stepPoints = 100;
  isLoadingImage = false;


  onImageSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    const file = input?.files?.[0];

    if (!file || !file.type.startsWith('image/')) {
      alert('Por favor selecciona una imagen válida.');
      return;
    }

    this.isLoadingImage = true;

    const reader = new FileReader();
    const img = new Image();

    reader.onload = () => {
      img.src = reader.result as string;

      img.onload = () => {
        setTimeout(() => {
          const canvas = this.canvasRef?.nativeElement;
          if (!canvas) return;

          const ctx = canvas.getContext('2d', { willReadFrequently: true });
          if (!ctx) return;

          canvas.width = img.width;
          canvas.height = img.height;
          ctx.drawImage(img, 0, 0);

          this.imageWidth = img.width;
          this.imageHeight = img.height;
          this.imageLoaded.set(true);
          this.isLoadingImage = false;
        }, 0); // Garantiza que el DOM se actualice
      };
    };

    reader.readAsDataURL(file);
  }

  calculateArea(): void {
    if (!this.imageLoaded()) return;

    const canvas = this.canvasRef.nativeElement;
    const ctx = canvas.getContext('2d', { willReadFrequently: true });
    if (!ctx) return;

    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
    const totalPixels = canvas.width * canvas.height;
    let ni = 0;

    for (let i = 0; i < this.numPoints; i++) {
      const x = Math.floor(Math.random() * canvas.width);
      const y = Math.floor(Math.random() * canvas.height);
      const index = (y * canvas.width + x) * 4;
      const r = imageData[index];
      const g = imageData[index + 1];
      const b = imageData[index + 2];

      // Suponemos blanco como mancha (255, 255, 255)
      if (r > 200 && g > 200 && b > 200) {
        ni++;
      }
    }

    const estimatedArea = (canvas.width * canvas.height) * (ni / this.numPoints);
    const result = {
      timestamp: new Date().toLocaleString(),
      area: estimatedArea,
      numPoints: this.numPoints
    };
    this.areaService.addResult(result);
    console.log(`Área estimada: ${estimatedArea.toFixed(2)} px² con ${this.numPoints} puntos`);
    // En siguiente paso lo enviaremos a la tabla
  }
}
