import { Component } from '@angular/core';

// ✅ IMPORTAR MODULOS DE ANGULAR MATERIAL
import { MatTabsModule } from '@angular/material/tabs';

// ✅ IMPORTAR COMPONENTES HIJOS
import { ImageUploadComponent } from './components/image-upload/image-upload.component';
import { AreaResultTableComponent } from './components/area-result-table/area-result-table.component';
import { MethodCarouselComponent } from './components/method-carousel/method-carousel.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    MatTabsModule,
    ImageUploadComponent,
    AreaResultTableComponent,
    MethodCarouselComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'frontend';
}
