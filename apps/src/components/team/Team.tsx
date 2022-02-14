import React, { useState, useEffect, useRef } from "react";
import { TTeam } from "./_types"
import styled from "@emotion/styled";
import { useParams } from "react-router-dom";


// pulls data and types it
async function getTeam(team_id: string): Promise<TTeam> {
    return fetch("/teams/" + team_id)
      .then(response => {
        if (!response.ok) {
          throw new Error(response.statusText)
        }
        return response.json()
      })
}

export const FlexContainer = styled.div({
     display: "flex",
     height: "150px"
});

const TeamTitle = (team: TTeam) => {
    return (
        <div style={{
            background: "lightgray"
        }}>
            <h1>{team.name}</h1>
        </div>
    )
}

const TeamHeader = (team: TTeam) => {
    return(
        <div style={{
            overflow: "hidden",
            position: "relative",
            background: "lightgray"
        }} > {
            <FlexContainer>
                <img 
                    ref={useRef<HTMLImageElement>(null)}
                    src={"https://www-league.nhlstatic.com/images/logos/teams-current-primary-light/" + team.id + ".svg"}
                    style={{height: "93%", width: "auto", border: "5px solid black", background: "white"}}
                />
            </FlexContainer>
        }
        </div>
    )
}

export default function Team ()  {
    let params = useParams();
    const [team, setTeam] = useState({} as TTeam);

    useEffect(() => {
        getTeam(String(params.teamId))
        .then((response) => {
            setTeam(response)
        })
    }, []);

    return (
        <div>
            {TeamTitle(team)}
            {TeamHeader(team)}
        </div>
    )
}
