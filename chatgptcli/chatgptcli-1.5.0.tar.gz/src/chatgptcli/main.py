#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

from .classes import openai as OpenAI
from .classes import chat as ChatHandler
from .classes import spinner as Spinner


class ChatGPT:
    def __init__(self, email, password):
        self.email = email
        self.password = password

        self.ACCESS_TOKEN: str or None = None
        self.TOKEN_EXPIRY: int or None = None
        self.CONVERSATION_UID: str or None = None
        self.PARENT_CONVERSATION_UID: int or None = None
        self.boot()

    def boot(self):
        if len(self.email) == 0 or len(self.password) == 0:
            raise Exception("Invalid email or password.") and print(
                "Invalid email or password."
            )
        if OpenAI.invalidToken():
            print("Generating a fresh Access Token")
            self.generateAccessToken()
        else:
            accessToken, expiry = OpenAI.accessToken()
            self.ACCESS_TOKEN = accessToken
            self.TOKEN_EXPIRY = expiry
            try:
                self.TOKEN_EXPIRY = int(self.TOKEN_EXPIRY)
            except Exception as e:
                raise Exception(e) and print(e)
            if self.TOKEN_EXPIRY < time.time():
                print("Generating a fresh Access Token")
                self.generateAccessToken()

    def generateAccessToken(self) -> bool:
        openAI = OpenAI.Auth(email_address=self.email, password=self.password)
        openAI.generateToken()
        expired = OpenAI.invalidToken()
        if expired:
            print("Invalid Access Token")
            return False
        return True

    def ask(self, prompt: str) -> str or None:
        if prompt is None:
            print("Enter a prompt.")
            raise Exception("Enter a prompt.")

        if not isinstance(prompt, str):
            raise Exception("Prompt must be a string.")

        if len(prompt) == 0:
            raise Exception("Prompt cannot be empty.")

        if OpenAI.invalidToken():
            print(
                "Access Invalid. Generating a fresh Access Token"
            )
            did_create = self.generateAccessToken()
            if did_create:
                print("GREEN}>> Successfully recreated access token.")
            else:
                print("Failed to recreate access token.")
                raise Exception("Failed to recreate access token.")

        accessToken = OpenAI.accessToken()
        answer, previous_convo, convo_id = ChatHandler.ask(
            auth_token=accessToken,
            prompt=prompt,
            conversation_id=self.CONVERSATION_UID,
            previous_convo_id=self.PARENT_CONVERSATION_UID,
        )
        if answer == "400" or answer == "401":
            print("Failed to get a response from the API.")
            return None

        self.CONVERSATION_UID = convo_id
        self.PARENT_CONVERSATION_UID = previous_convo
        return answer

    def chat(self):
        """
        Start a CLI chat session.
        :param prompt:
        :return:
        """
        # Check if the access token is expired
        if OpenAI.invalidToken():
            print(
                "Access Invalid. Generating a fresh Access Token"
            )
            did_create = self.generateAccessToken()
            if did_create:
                print("GREEN}>> Successfully recreated access token.")
            else:
                print("Failed to recreate access token.")
                raise Exception("Failed to recreate access token.")
        else:
            print("ChatGPT Session Started.")

        accessToken = OpenAI.accessToken()

        while True:
            try:
                prompt = input("You: ")
                spinner = Spinner.Spinner()
                spinner.start("ChatGPT is typing...")
                answer, previous_convo, convo_id = ChatHandler.ask(
                    auth_token=accessToken,
                    prompt=prompt,
                    conversation_id=self.CONVERSATION_UID,
                    previous_convo_id=self.PARENT_CONVERSATION_UID,
                )
                if answer == "400" or answer == "401":
                    print("Failed to get a response from the API.")
                    return None
                self.CONVERSATION_UID = convo_id
                self.PARENT_CONVERSATION_UID = previous_convo
                spinner.stop()
                print("ChatGPT: " + answer)
            except KeyboardInterrupt:
                print("Exiting...")
                break
