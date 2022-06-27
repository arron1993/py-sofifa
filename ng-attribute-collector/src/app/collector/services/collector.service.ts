import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CollectorService {

  constructor(private http: HttpClient) { }

  upload(collector: any) {
    return this.http.post(`${environment.apiEndpoint}/api/collector/`, collector)
  }
}
