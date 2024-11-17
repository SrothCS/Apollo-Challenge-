from api.routes import app, initialize_database

if __name__ == "__main__":
    try:
        initialize_database()
    except Exception as e:
        print(f"Failed to initialize database: {e}")
    app.run(debug=True)
