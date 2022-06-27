import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CollectorIndexPageComponent } from './collector-index-page.component';

describe('CollectorIndexPageComponent', () => {
  let component: CollectorIndexPageComponent;
  let fixture: ComponentFixture<CollectorIndexPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CollectorIndexPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CollectorIndexPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
