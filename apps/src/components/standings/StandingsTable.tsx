import { useState, useEffect } from "react";
import { TStanding } from "./_types";

const COLUMNS = ["Team", "GP", "W", "L", "ROW", "Points", "Points Percentage"]


function _StandingsTableRow(standing: TStanding, idx: number) {
    return (
        <tr key={idx}>
            <td>{standing.teamName}</td>
            <td>{standing.gamesPlayed}</td>
            <td>{standing.regulationWins}</td>
            <td>{standing.gamesPlayed - standing.row}</td>
            <td>{standing.row}</td>
            <td>{standing.points}</td>
            <td>{standing.pointsPercentage}</td>
        </tr>
    )
}

export default function StandingsTable(standings: Array<TStanding>) {
    if(!standings) return null;
    return (
        <table>
            <thead>
                <tr>{standings[0].divisionName}</tr>
                <tr>
                    <th />
                    {Object.values(COLUMNS).map((col, idx) => (
                        <th key={idx}>{col}</th>
                    ))}
                </tr>
            </thead>
            <tbody>
                {
                    standings.sort((standingA, standingB) => (standingA.pointsPercentage > standingB.pointsPercentage) ? -1 : 1)
                    .map((value, idx) => {
                        return _StandingsTableRow(value, idx)
                    })
                }
            </tbody>
        </table>
    )
}