import React from "react";
import { TPlayer } from "./_types"
import { Table, TableHead, TableRow, TableCell, TableContainer, TableBody, Paper } from "@material-ui/core";

const COLUMN_MAP = {
    "Number": "primaryNumber",
    "Name": "fullName",
    "Age": "currentAge",
}

interface TeamRosterTableProps {
    players: TPlayer[],
}

export const TeamRosterTable: React.FC<TeamRosterTableProps> = (props: TeamRosterTableProps) => {
    const players = props.players;
    return (
        <TableContainer component={Paper}>
            <Table aria-label="simple table">
                <TableHead>
                    <TableRow>{
                        Object.keys(COLUMN_MAP).map((col) => {
                            return <TableCell align="left">{col}</TableCell>
                        })
                    }
                    </TableRow>
                </TableHead>
                <TableBody>
                    {
                        players.sort((playerA, playerB) => (playerA.primaryNumber > playerB.primaryNumber) ? 1 : -1)
                        .map((player, idx) => {
                            return (
                                <TableRow key={idx}>
                                    {
                                        Object.values(COLUMN_MAP).map((col) => {
                                            return <TableCell>{col in player ? player[col] : ""}</TableCell>
                                        })
                                    }
                                </TableRow>
                            )
                        })
                            
                    }
                </TableBody>
            </Table>
        </TableContainer>
    )
}