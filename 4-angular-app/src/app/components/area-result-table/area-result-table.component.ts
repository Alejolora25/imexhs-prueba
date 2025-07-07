import { Component, computed, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AreaResultService } from '../../services/area-result.service';
import { MatCardModule } from '@angular/material/card';
import { MatTableModule } from '@angular/material/table';

@Component({
  selector: 'app-area-result-table',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatTableModule],
  templateUrl: './area-result-table.component.html',
  styleUrl: './area-result-table.component.scss'
})
export class AreaResultTableComponent {
  displayedColumns: string[] = ['timestamp', 'area', 'numPoints'];

  private areaService = inject(AreaResultService);
  results = computed(() => [...this.areaService.results()].reverse());
}
