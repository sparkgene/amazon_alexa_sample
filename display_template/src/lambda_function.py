# -*- coding: utf-8 -*-
import os

BUCKET_DOMAIN = os.environ["BUCKET_DOMAIN"]
MEDIA_BUCKET = os.environ["MEDIA_BUCKET"]
MEDIA_URL = "https://{}.amazonaws.com/{}/{}"

SESSION_BODY_1 = "body_1"
SESSION_BODY_2 = "body_2"
SESSION_BODY_3 = "body_3"
SESSION_BODY_6 = "body_6"
SESSION_BODY_7 = "body_7"
SESSION_LIST_1 = "list_1"
SESSION_LIST_2 = "list_2"
SESSION_VIDEO = "video"
SESSION_ACTION_1 = "act_1"

def lambda_handler(event, context):
    print(event)

    if event["request"]["type"] == "LaunchRequest":
        print("on_launch")
        return help()
    elif event["request"]["type"] == "IntentRequest":
        if event["request"]["intent"]["name"] == "BodyTemplate":
            return body_template(event["request"]["intent"]["slots"]["number"]["value"])
        elif event["request"]["intent"]["name"] == "ListTemplate":
            return list_template(event["request"]["intent"]["slots"]["number"]["value"])
        elif event["request"]["intent"]["name"] == "VideoTemplate":
            return video_template()
        elif event["request"]["intent"]["name"] == "ActionSample":
            return action_sample()
        elif event["request"]["intent"]["name"] == "AMAZON.YesIntent":
            ses = event["session"]["attributes"]["template"].split("_")
            print(ses)
            if ses[0] == "body":
                return body_template(ses[1])
            elif ses[0] == "list":
                return list_template(ses[1])
            elif ses[0] == "video":
                return video_template()
            elif ses[0] == "act":
                return action_sample()
            else:
                return help()
        elif event["request"]["intent"]["name"] == "AMAZON.NoIntent":
            return goodby()
    elif event["request"]["type"] == "Display.ElementSelected":
        return item_selected(event["context"]["Display"]["token"], event["request"]["token"])


    print("request type unmatch")
    return help()

def help():
    title = "Echo Show Display Test"
    speech = "This is a sample Skill for testing Echo Show display templates."
    directives = [
        {
            "type": "Hint",
            "hint": {
                "type": "PlainText",
                "text": "show body template number 1"
            }
        }
    ]

    return build_speechlet_response(title, speech, directives, SESSION_BODY_1)

def goodby():

    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "good by."
            },
            "shouldEndSession": True
        }
    }
    print(response)
    return response

def body_template(number):
    print("body_template {}".format(number))

    if number == "1":
        return body_template_one()
    elif number == "2":
        return body_template_two()
    elif number == "3":
        return body_template_three()
    elif number == "6":
        return body_template_six()
    elif number == "7":
        return body_template_seven()

    return help()

def list_template(number):
    print("list_template {}".format(number))

    if number == "1":
        return list_template_one()
    elif number == "2":
        return list_template_two()

    return help()

## --------- body template ---------
def body_template_one():
    title = "This is BodyTemplate 1"
    speech = "This is body template one."
    primary_text = "body template can show three lines of text."
    secondary_text = "you can change font size."
    tertiary_text = "If the sentence is too long than the width, it will be Wrapped. this part will be shown on next row. If the text is very long you can scroll to see the full text."
    speech = " ".join([speech, primary_text, secondary_text, tertiary_text])

    template = {
        "type": "Display.RenderTemplate",
        "template": {
            "type": "BodyTemplate1",
            "token": "bt1",
            "backButton": "HIDDEN",
            "backgroundImage": {
                "contentDescription": "Mt Fuji",
                "sources": [
                    {
                        "url": media_url("background-1.jpg")
                    }
                ]
            },
            "title": "This is BodyTemplate1",
            "textContent": {
                "primaryText": {
                    "text": primary_text,
                    "type": "PlainText"
                },
                "secondaryText": {
                    "text": "<font size='7'>" + secondary_text + "</font>",
                    "type": "RichText"
                },
                "tertiaryText": {
                    "text": tertiary_text,
                    "type": "PlainText"
                }
            }
        }
    }

    directives = [
        template
    ]

    return build_speechlet_response(title, speech, directives, SESSION_BODY_2)

def body_template_two():
    title = "This is BodyTemplate 2"
    speech = "This is body template two."
    primary_text = "body template can show three lines of text."
    secondary_text = "you can change font size."
    tertiary_text = "body template two can not scroll. If the text is too long it will truncated."
    speech = " ".join([speech, primary_text, secondary_text, tertiary_text])

    template = {
        "type": "Display.RenderTemplate",
        "template": {
            "type": "BodyTemplate2",
            "token": "bt2",
            "backButton": "VISIBLE",
            "backgroundImage": {
                "contentDescription": "Mt Fuji",
                "sources": [
                    {
                        "url": media_url("background-1.jpg")
                    }
                ]
            },
            "title": title,
            "image": {
                "contentDescription": "BBQ gril",
                "sources": [
                    {
                        "url": media_url("280x280.jpg")
                    }
                ]
            },
            "textContent": {
                "primaryText": {
                    "text": primary_text,
                    "type": "PlainText"
                },
                "secondaryText": {
                    "text": "<font size='7'>" + secondary_text + "</font>",
                    "type": "RichText"
                },
                "tertiaryText": {
                    "text": tertiary_text,
                    "type": "PlainText"
                }
            }
        }
    }

    hint = {
        "type": "Hint",
        "hint": {
            "type": "PlainText",
            "text": "tell invocation name body template number 3"
        }
    }

    directives = [
        template,
        hint
    ]

    return build_speechlet_response(title, speech, directives, SESSION_BODY_3)

def body_template_three():
    title = "This is BodyTemplate 3"
    speech = "This is body template three."
    primary_text = "body template three show image on the left side."
    secondary_text = "you can change font size."
    tertiary_text = "body template three can contain 8000 characters. If the text is very long, it become scrollable. Some long text here. Some long text here. Some long text here. Some long text here."
    speech = " ".join([speech, primary_text, secondary_text, tertiary_text])

    template = {
        "type": "Display.RenderTemplate",
        "template": {
            "type": "BodyTemplate3",
            "token": "bt3",
            "backButton": "VISIBLE",
            "backgroundImage": {
                "contentDescription": "Mt Fuji",
                "sources": [
                    {
                        "url": media_url("background-1.jpg")
                    }
                ]
            },
            "title": title,
            "image": {
                "contentDescription": "BBQ gril",
                "sources": [
                    {
                        "url": media_url("280x280.jpg")
                    }
                ]
            },
            "textContent": {
                "primaryText": {
                    "text": primary_text,
                    "type": "PlainText"
                },
                "secondaryText": {
                    "text": "<font size='7'>" + secondary_text + "</font>",
                    "type": "RichText"
                },
                "tertiaryText": {
                    "text": tertiary_text,
                    "type": "PlainText"
                }
            }
        }
    }

    # body template 3 do not show hint
    directives = [
        template
    ]

    return build_speechlet_response(title, speech, directives, SESSION_BODY_6)

def body_template_six():
    title = "This is body template six."
    primary_text = "body template six overlay the text."
    secondary_text = "body template six can be used as a welcome screen to offer guidance."
    tertiary_text = "non-scroll and PlainText only"
    speech = " ".join([title, primary_text, secondary_text, tertiary_text])

    template = {
        "type": "Display.RenderTemplate",
        "template": {
            "type": "BodyTemplate6",
            "token": "bt6",
            "backButton": "VISIBLE",
            "backgroundImage": {
                "contentDescription": "Mt Fuji",
                "sources": [
                    {
                        "url": media_url("background-1.jpg")
                    }
                ]
            },
            "textContent": {
                "primaryText": {
                    "text": primary_text,
                    "type": "PlainText"
                },
                "secondaryText": {
                    "text": secondary_text,
                    "type": "PlainText"
                },
                "tertiaryText": {
                    "text": tertiary_text,
                    "type": "PlainText"
                }
            }
        }
    }

    hint = {
        "type": "Hint",
        "hint": {
            "type": "PlainText",
            "text": "tell invocation name body template number 7"
        }
    }

    directives = [
        template,
        hint
    ]

    return build_speechlet_response(title, speech, directives, SESSION_BODY_7)

def body_template_seven():
    title = "This is body template seven."
    primary_text = "body template seven overlay image."
    secondary_text = "body template seven can not show any text."
    speech = " ".join([title, primary_text, secondary_text])

    template = {
        "type": "Display.RenderTemplate",
        "template": {
            "type": "BodyTemplate7",
            "token": "bt7",
            "title": title,
            "backButton": "VISIBLE",
            "backgroundImage": {
                "contentDescription": "Mt Fuji",
                "sources": [
                    {
                        "url": media_url("background-1.jpg")
                    }
                ]
            },
            "image": {
                "contentDescription": "view from the farm",
                "sources": [
                    {
                        "url": media_url("foreground.jpg")
                    }
                ]
            }
        }
    }

    hint = {
        "type": "Hint",
        "hint": {
            "type": "PlainText",
            "text": "tell invocation name list template number 1"
        }
    }

    directives = [
        template,
        hint
    ]

    return build_speechlet_response(title, speech, directives, SESSION_LIST_1)


## --------- list template ---------

def list_template_one():
    title = "This is ListTemplate 1"
    speech = "List template one is good for Static or dynamically-generated search results, menu selection, lists, instructions, directions. Say scroll down or up to scroll. Or page down or pageup"

    template = {
        "type": "Display.RenderTemplate",
        "template": {
            "type": "ListTemplate1",
            "token": "list_template_one",
            "title": title,
            "backButton": "VISIBLE",
            "backgroundImage": {
                "contentDescription": "Mt Fuji",
                "sources": [
                    {
                        "url": media_url("background-2.jpg")
                    }
                ]
            },
            "listItems": [
                {
                    "token": "item_1",
                    "image": {
                        "sources": [
                            {
                            "url": media_url("88x88-1.jpg")
                            }
                        ],
                        "contentDescription": "strawberry jam"
                    },
                    "textContent": {
                        "primaryText": {
                            "type": "PlainText",
                            "text": "Primary text is here"
                        },
                        "secondaryText": {
                            "type": "PlainText",
                            "text": "Secondary Text"
                        }
                    }
                },
                {
                    "token": "item_2",
                    "image": {
                        "sources": [
                            {
                            "url": media_url("88x88-2.jpg")
                            }
                        ],
                        "contentDescription": "garlic oil"
                    },
                    "textContent": {
                        "primaryText": {
                            "type": "PlainText",
                            "text": "Font size is large."
                        },
                        "secondaryText": {
                            "type": "PlainText",
                            "text": "Scrollable by touch and voice"
                        }
                    }
                },
                {
                    "token": "item_2",
                    "textContent": {
                        "primaryText": {
                            "type": "PlainText",
                            "text": "Image is Optional"
                        },
                        "secondaryText": {
                            "type": "PlainText",
                            "text": "Non-expandable text area"
                        }
                    }
                },
                {
                    "token": "item_4",
                    "image": {
                        "sources": [
                            {
                            "url": media_url("88x88-2.jpg")
                            }
                        ],
                        "contentDescription": "garlic oil"
                    },
                    "textContent": {
                        "primaryText": {
                            "type": "PlainText",
                            "text": "PlainText type"
                        },
                        "secondaryText": {
                            "type": "PlainText",
                            "text": "Secondary Text"
                        }
                    }
                }

            ]
        }
    }

    # list template 1 do not show hint
    directives = [
        template
    ]

    return build_speechlet_response(title, speech, directives, SESSION_LIST_2)

def list_template_two():
    title = "This is ListTemplate 2"
    speech = "List template two is good for Static or dynamically-generated search results, menu selection, lists. Say scroll right or left to scroll."

    template = {
        "type": "Display.RenderTemplate",
        "template": {
            "type": "ListTemplate2",
            "token": "list_template_two",
            "title": title,
            "backButton": "VISIBLE",
            "backgroundImage": {
                "contentDescription": "Mt Fuji",
                "sources": [
                    {
                        "url": media_url("background-2.jpg")
                    }
                ]
            },
            "listItems": [
                {
                    "token": "item_1",
                    "image": {
                        "sources": [
                            {
                            "url": media_url("280x192.jpg")
                            }
                        ],
                        "contentDescription": "strawberry jam"
                    },
                    "textContent": {
                        "primaryText": {
                            "type": "PlainText",
                            "text": "Primary text is here"
                        },
                        "secondaryText": {
                            "type": "PlainText",
                            "text": "Secondary Text"
                        }
                    }
                },
                {
                    "token": "item_2",
                    "image": {
                        "sources": [
                            {
                            "url": media_url("280x192.jpg")
                            }
                        ],
                        "contentDescription": "garlic oil"
                    },
                    "textContent": {
                        "primaryText": {
                            "type": "PlainText",
                            "text": "Font size is large."
                        },
                        "secondaryText": {
                            "type": "PlainText",
                            "text": "Scrollable by touch and voice"
                        }
                    }
                },
                {
                    "token": "item_2",
                    "image": {
                        "sources": [
                            {
                            "url": media_url("280x192.jpg")
                            }
                        ],
                        "contentDescription": "strawberry jam"
                    },
                    "textContent": {
                        "primaryText": {
                            "type": "PlainText",
                            "text": "Good for title"
                        },
                        "secondaryText": {
                            "type": "PlainText",
                            "text": "Non-expandable text area"
                        }
                    }
                },
                {
                    "token": "item_4",
                    "image": {
                        "sources": [
                            {
                            "url": media_url("280x192.jpg")
                            }
                        ],
                        "contentDescription": "garlic oil"
                    },
                    "textContent": {
                        "primaryText": {
                            "type": "PlainText",
                            "text": "PlainText type"
                        },
                        "secondaryText": {
                            "type": "PlainText",
                            "text": "Secondary Text"
                        }
                    }
                }

            ]
        }
    }

    directives = [
        template
    ]

    return build_speechlet_response(title, speech, directives, SESSION_ACTION_1)


## --------- video ---------

def video_template():

    video_template = {
        "type": "VideoApp.Launch",
        "videoItem":
        {
            "source": media_url("alexa_test.mp4"),
            "metadata": {
                "title": "Title for Sample Video",
                "subtitle": "Secondary Title for Sample Video"
            }
        }
    }

    primary_text = "Other template can use after video"
    secondary_text = "But you can not use speech and hint."

    body_template = {
        "type": "Display.RenderTemplate",
        "template": {
            "type": "BodyTemplate6",
            "token": "bt6",
            "backButton": "VISIBLE",
            "backgroundImage": {
                "contentDescription": "Mt Fuji",
                "sources": [
                    {
                        "url": media_url("background-1.jpg")
                    }
                ]
            },
            "textContent": {
                "primaryText": {
                    "text": primary_text,
                    "type": "PlainText"
                },
                "secondaryText": {
                    "text": secondary_text,
                    "type": "PlainText"
                }
            }
        }
    }

    directives = [
        video_template,
        body_template
    ]

    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": None,
            "card": {
                'type': 'Simple',
                'title': "video player",
                'content': "this template play video."
            },
            "directives": directives
        }
    }
    print(response)
    return response

## --------- action sample ---------

def action_sample():
    title = "RichText can include action."
    primary_text = "Clicking the word cancel invoke event."
    secondary_text = "<action value='cancel_action'>Cancel</action>"
    speech = " ".join([title, primary_text])

    template = {
        "type": "Display.RenderTemplate",
        "template": {
            "type": "BodyTemplate1",
            "token": "action1",
            "backButton": "HIDDEN",
            "title": title,
            "textContent": {
                "primaryText": {
                    "text": primary_text,
                    "type": "PlainText"
                },
                "secondaryText": {
                    "text": secondary_text,
                    "type": "RichText"
                }
            }
        }
    }

    directives = [
        template
    ]

    return build_speechlet_response(title, speech, directives, SESSION_VIDEO)

def item_selected(context_token, token):
    action_map = {
        "action1": "Action sample",
        "list_template_one": "list tepmlate 1",
        "list_template_two": "list tepmlate 2"
    }
    title = "Action Invoked."
    primary_text = "action invoked from {}. the token is {}.".format(
        action_map[context_token],
        token
    )

    template = {
        "type": "Display.RenderTemplate",
        "template": {
            "type": "BodyTemplate1",
            "token": "action2",
            "backButton": "HIDDEN",
            "title": title,
            "textContent": {
                "primaryText": {
                    "text": primary_text,
                    "type": "PlainText"
                }
            }
        }
    }

    directives = [
        template
    ]

    return build_speechlet_response(title, primary_text, directives, SESSION_BODY_1)


## --------- helper methods ---------

def media_url(key):
    return MEDIA_URL.format(BUCKET_DOMAIN, MEDIA_BUCKET, key)

def build_speechlet_response(title, speech, directives, phase):

    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "{}. do you want to see the next template?".format(speech)
            },
            "card": {
                'type': 'Simple',
                'title': title,
                'content': speech
            },
            "directives": directives,
            "shouldEndSession": False
        },
        "sessionAttributes": {
            "template": phase
        }
    }
    print(response)
    return response
