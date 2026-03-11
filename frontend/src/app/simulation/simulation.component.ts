import { Component } from '@angular/core';
import { SimulationService } from '../services/simulation.service';

@Component({
  selector: 'app-simulation',
  templateUrl: './simulation.component.html',
  styleUrls: ['./simulation.component.css']
})
export class SimulationComponent {

  reward:number = 0;

  constructor(private simService:SimulationService){}

  runSimulation(){

    this.simService.getSimulation().subscribe(data => {

      this.reward = data.reward;

      console.log("Frame data:",data.frame);

    });

  }

}