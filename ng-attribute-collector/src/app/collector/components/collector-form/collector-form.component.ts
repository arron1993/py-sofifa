import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { CollectorService } from '../../services/collector.service';

@Component({
  selector: 'app-collector-form',
  templateUrl: './collector-form.component.html',
  styleUrls: ['./collector-form.component.scss']
})
export class CollectorFormComponent implements OnInit {
  @Output() onUpload = new EventEmitter<string>()

  file: any = null;
  imgPreview: any = null;

  constructor(private cs: CollectorService) { }

  ngOnInit(): void {
  }

  onChange(event: any) {
    const reader = new FileReader();
    this.file = event.target.files[0];
    reader.onloadend = () => { this.imgPreview = reader.result }
    reader.readAsDataURL(this.file);
  }

  onSubmit() {
    this.cs.upload(this.file).subscribe((resp: any) => {
      this.onUpload.emit(resp)
    })
  }

   getImage() {

  }
}
