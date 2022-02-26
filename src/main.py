#!/usr/bin/env python
import notify2

notify2.init('Notifications App')

n = notify2.Notification("Summary", "Notification body", "Notification icon")

n.show()
