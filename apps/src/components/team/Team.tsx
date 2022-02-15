import React, { useState, useEffect, useRef } from "react";
import { TTeam } from "./_types"
import styled from "@emotion/styled";
import { useParams } from "react-router-dom";
import { Card, CardContent, CardMedia, Typography } from "@material-ui/core"


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

export const HorizontalFlexContainer = styled.div({
     display: "flex",
     justifyContent: "center",
     flexDirection: "row",
     height: "150px",
     css: {
        width: "100%"
     }
});

export const VerticalFlexContainer = styled.div({
     display: "flex",
     flexDirection: "column",
     height: "150px",
     color: "white",
     backgroundColor: "black"
});

const TeamTitle = (team: TTeam) => {
    return (
        <HorizontalFlexContainer><h1>{team.name}</h1></HorizontalFlexContainer>
    )
}

const TeamHeaderCard = (title: string, content: string) => {
    return (
        <Card>
            <CardContent>
                <Typography align="center" color="textSecondary">{title}</Typography>
                <Typography align="center" color="textPrimary" variant="h4">{content}</Typography>
            </CardContent>
        </Card>
    )
}

const TeamHeader = (team: TTeam) => {
    return(
        <HorizontalFlexContainer>
            <Card>
                <CardMedia
                    component="img"
                    height="150"
                    image={"https://www-league.nhlstatic.com/images/logos/teams-current-primary-light/" + String(team.id) + ".svg"}
                />
            </Card>
            {TeamHeaderCard("VENUE", team.venueName)}
            {TeamHeaderCard("DIVISION", team.divisionName)}
            {TeamHeaderCard("CONFERENCE", team.conferenceName)}
            {TeamHeaderCard("FIRST YEAR OF PLAY", String(team.firstYearOfPlay))}
        </HorizontalFlexContainer>
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
        <VerticalFlexContainer>
            {TeamTitle(team)}
            {TeamHeader(team)}
        </VerticalFlexContainer>
    )
}
