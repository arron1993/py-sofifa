import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'collector',
    loadChildren: () =>
      import('./collector/collector-routing.module').then(
        (m) => m.CollectorRoutingModule
      ),
  },
  {
    path: '',
    redirectTo: 'collector',
    pathMatch: 'full',
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
