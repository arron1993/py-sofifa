import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CollectorRoutingModule } from './collector-routing.module';
import { CollectorIndexPageComponent } from './pages/collector-index-page/collector-index-page.component';
import { CollectorFormComponent } from './components/collector-form/collector-form.component';
import { FormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    CollectorIndexPageComponent,
    CollectorFormComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    CollectorRoutingModule
  ]
})
export class CollectorModule { }
