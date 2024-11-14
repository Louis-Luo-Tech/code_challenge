#!/usr/bin/env python3
import aws_cdk as cdk
from stack import ThumbnailStack

app = cdk.App()
ThumbnailStack(app, "ThumbnailStack")
app.synth()
