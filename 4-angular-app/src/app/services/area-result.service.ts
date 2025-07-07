import { Injectable, signal } from '@angular/core';

export interface AreaResult {
  timestamp: string;
  area: number;
  numPoints: number;
}

@Injectable({ providedIn: 'root' })
export class AreaResultService {
  private resultsSignal = signal<AreaResult[]>([]);

  get results() {
    return this.resultsSignal.asReadonly();
  }

  addResult(result: AreaResult) {
    const current = this.resultsSignal();
    this.resultsSignal.set([result, ...current]); // agrega al principio
  }

  clearResults() {
    this.resultsSignal.set([]);
  }
}
