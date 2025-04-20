#  External Service Integration in Python

This repository demonstrates a clean and extensible architecture for integrating external services in Python using well-established design patterns.


## Design Overview

- **Strategy Pattern**: Enables interchangeable drivers (real or dummy) for communication with external service.
- **Factory Pattern**: Decides which driver to use based on the current environment.
- **Singleton Pattern**: Ensures a single, reusable instance of the service client throughout the application.

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` File

You can optionally add the following to your `.env` file:

```env
WEATHER_PROVIDER=real
```

The decouple package will automatically load environment variables from the `.env` file, and if not found, it will use the default value which is `dummy`.

### Run the Client

```bash
python main.py
```

## Feedback

I’d love to hear your thoughts on this approach.  
Share your feedback, alternative ideas, or improvements you’ve made in your own projects!

---
