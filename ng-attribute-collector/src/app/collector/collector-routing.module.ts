import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CollectorIndexPageComponent } from './pages/collector-index-page/collector-index-page.component';

const routes: Routes = [{
  path: '',
  component: CollectorIndexPageComponent
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CollectorRoutingModule { }
