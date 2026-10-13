import os
import streamlit.components.v1 as components

_parent_dir = os.path.dirname(os.path.abspath(__file__))

_keystroke_path = os.path.join(_parent_dir, "keystroke_plugin")
keystroke_plugin = components.declare_component("keystroke_plugin", path=_keystroke_path)

_plugin_path = os.path.join(_parent_dir, "enrollment_plugin")
enrollment_plugin = components.declare_component("enrollment_plugin", path=_plugin_path)

_free_typing_path = os.path.join(_parent_dir, "free_typing_plugin")
free_typing_plugin = components.declare_component("free_typing_plugin", path=_free_typing_path)