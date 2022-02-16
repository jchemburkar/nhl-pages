import React, { useState, useEffect, useRef } from "react";
import { TTeam, TPlayer } from "./_types"
import { TeamRosterTable } from "./TeamRosterTable"
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

/*
    STYLES
*/

const HeaderContainer = styled.div({
     display: "flex",
     justifyContent: "center",
     flexDirection: "row",
     alignItems: "center"
});

const HorizontalFlexContainer = styled.div({
     display: "flex",
     justifyContent: "center",
     flexDirection: "row"
});

const VerticalFlexContainer = styled.div({
     display: "flex",
     flexDirection: "column",
     height: "250px",
     color: "white",
     backgroundColor: "black",
     paddingBottom: "30px"
});

const ElementSpacingStyle = {
    "paddingRight": "4%",
    "paddingLeft": "0px"
}

/*
    COMPONENTS
*/

const TeamTitle = (team: TTeam) => {
    return (
        <HorizontalFlexContainer><h1>{team.name}</h1></HorizontalFlexContainer>
    )
}

const TeamHeaderCard = (title: string, content: string) => {
    return (
        <div style={{"paddingRight": "0.5%"}}>
            <Card>
                <CardContent>
                    <Typography align="center" color="textSecondary">{title}</Typography>
                    <Typography align="center" color="textPrimary" variant="h4">{content}</Typography>
                </CardContent>
            </Card>
        </div>
    )
}

const TeamHeader = (team: TTeam) => {
    return(
        <HeaderContainer>
            <div style={{"paddingRight": "0.5%"}}>
                <Card>
                    <CardMedia
                        component="img"
                        height="150"
                        image={"https://www-league.nhlstatic.com/images/logos/teams-current-primary-light/" + String(team.id) + ".svg"}
                    />
                </Card>
            </div>
            {TeamHeaderCard("VENUE", team.venueName)}
            {TeamHeaderCard("DIVISION", team.divisionName)}
            {TeamHeaderCard("CONFERENCE", team.conferenceName)}
            {TeamHeaderCard("FIRST YEAR OF PLAY", String(team.firstYearOfPlay))}
        </HeaderContainer>
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
            <VerticalFlexContainer>
                {TeamTitle(team)}
                {TeamHeader(team)}
            </VerticalFlexContainer>
            <HorizontalFlexContainer>
                <div style={ElementSpacingStyle}>
                    <h1 style={{textAlign: "center"}}>Forwards</h1>
                    <TeamRosterTable players={team.players ? Object.values(team.players).filter(player => ["C", "L", "R"].includes(player.primaryPosition)) : Array<TPlayer>()}/>
                </div>
                <div style={ElementSpacingStyle}>
                    <h1 style={{textAlign: "center"}}>Defenseman</h1>
                    <TeamRosterTable players={team.players ? Object.values(team.players).filter(player => ["D"].includes(player.primaryPosition)) : Array<TPlayer>()}/>
                </div>
                <div style={ElementSpacingStyle}>
                    <h1 style={{textAlign: "center"}}>Goalies</h1>
                    <TeamRosterTable players={team.players ? Object.values(team.players).filter(player => ["G"].includes(player.primaryPosition)) : Array<TPlayer>()}/>
                </div>
            </HorizontalFlexContainer>
        </div>
    )
}
