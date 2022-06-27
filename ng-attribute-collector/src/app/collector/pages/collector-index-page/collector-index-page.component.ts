import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-collector-index-page',
  templateUrl: './collector-index-page.component.html',
  styleUrls: ['./collector-index-page.component.scss']
})
export class CollectorIndexPageComponent implements OnInit {
  results = "";
  constructor() { }

  ngOnInit(): void {
  }

}
