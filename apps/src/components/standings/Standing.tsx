import { useState, useEffect } from "react";
import { TStanding } from "./_types";
import StandingsTable from "./StandingsTable"

// pulls data and types it
async function getStandings(): Promise<Array<TStanding>> {
    return fetch("/standings")
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText)
        }
        return response.json()
      })
}

const groupDivisions = (standings: Array<TStanding>): Array<Array<TStanding>> =>  {
    return standings.reduce((divisions, standing) => {
        if (!divisions[standing.divisionName]) divisions[standing.divisionName] = Array<TStanding>();
        divisions[standing.divisionName].push(standing);
        return divisions;
    }, Object())
}

export default function Standings ()  {
    const [ standings, setStandings ] = useState(Array<TStanding>());

    useEffect(() => {
        getStandings()
        .then((response) => {
                setStandings(response);
            }
        );
    }, []);

    return <div>
        {
            Object.values(groupDivisions(standings))
            .map((division: Array<TStanding>) => StandingsTable(division))
        }
    </div>
}