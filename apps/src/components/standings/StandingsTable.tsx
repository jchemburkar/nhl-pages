import React, { useState, useEffect } from "react";
import { TStanding } from "./_types";
import Table from "@material-ui/core/Table";
import { TableHead, TableRow, TableCell, TableContainer, TableBody, Paper } from "@material-ui/core";

const COLUMN_MAP = {
    "Team": "teamName",
    "GP": "gamesPlayed",
    "W": "regulationWins",
    "ROW": "row",
    "Points": "points",
    "Points Pct": "pointsPercentage"
}

export default function StandingsTable(standings: Array<TStanding>) {
    if(!standings) return null;
    
    return (
        <div>
            <h1 style={{font: "aria", textAlign: "center"}}>{standings[0].divisionName}</h1>
            <TableContainer component={Paper}>
                <Table aria-label="simple table">
                    <TableHead>
                        <TableRow>{
                            Object.keys(COLUMN_MAP).map((col) => {
                                return <TableCell align="right">{col}</TableCell>
                            })
                        }
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {
                            standings.sort((standingA, standingB) => (standingA.points > standingB.points) ? -1 : 1)
                            .map((standing, idx) => {
                                return (
                                    <TableRow key={idx}>
                                        {
                                            Object.values(COLUMN_MAP).map((col) => {
                                                return <TableCell>{col in standing ? standing[col] : ""}</TableCell>
                                            })
                                        }
                                    </TableRow>
                                )
                            })
                                
                        }
                    </TableBody>
                </Table>
            </TableContainer>
        </div>
    )
}