import { Component, OnInit } from '@angular/core';
import { Stats } from '../../classes/stats';


@Component({
  selector: 'app-collector-index-page',
  templateUrl: './collector-index-page.component.html',
  styleUrls: ['./collector-index-page.component.scss']
})
export class CollectorIndexPageComponent implements OnInit {
  results: Stats|null = null;

  constructor() { }

  ngOnInit(): void {
  }

}
