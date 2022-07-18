export class Stats {
    sprint_speed : number  = 0
    finishing: number  = 0
    vision: number = 0
    agility: number = 0
    interceptions: number = 0
    jumping: number = 0
    acceleration: number = 0
    att_position: number = 0
    crossing: number = 0
    balance: number = 0
    heading_acc: number = 0
    stamina: number = 0
    shot_power: number = 0
    fk_acc: number = 0
    reactions: number = 0
    def_aware: number = 0
    strength: number = 0
    long_shots: number = 0
    long_pass: number = 0
    composure: number = 0
    stand_tackle: number = 0
    aggression: number = 0
    penalties: number = 0
    short_pass: number = 0
    ball_control: number = 0
    slide_tackle: number = 0
    volleys: number = 0
    curve: number = 0
    dribbling: number = 0

    constructor(args: any) {
        for (let key in args) {
            if (args[key] !== null) {
                args[key] = parseInt(args[key], 10)
            } else {
                args[key] = 0
            }


        }
        Object.assign(this, args)
    }

    getPace() {
        return Math.round((this.sprint_speed + this.acceleration) / 2)
    }

    getShooting() {
        return Math.round((
            this.finishing +
            this.att_position +
            this.shot_power +
            this.long_shots +
            this.penalties +
            this.volleys) / 6)
    }

    getPassing() {
        return Math.round((
            this.vision +
            this.crossing +
            this.fk_acc +
            this.long_pass +
            this.short_pass +
            this.curve
        ) / 6)
    }

    getDribbling() {
        return Math.round((
            this.agility +
            this.balance +
            this.reactions +
            this.composure +
            this.ball_control +
            this.dribbling
        ) / 6)
    }

    getDefending() {
        return Math.round((
            this.interceptions +
            this.heading_acc +
            this.def_aware +
            this.stand_tackle +
            this.slide_tackle
        ) / 5)
    }

    getPhysical() {
        return Math.round((
            this.jumping +
            this.stamina +
            this.strength +
            this.aggression
        ) / 4)
    }
}
