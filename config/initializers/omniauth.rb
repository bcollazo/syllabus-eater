Rails.application.config.middleware.use OmniAuth::Builder do
  provider :google_oauth2, "754039179110-2lrtbub7rh2otsid63d8f1m217gkbfr8.apps.googleusercontent.com", "2beMSu7LzBqeowVo-Mj0kP06", {
    access_type: 'offline',
    scope: 'https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/calendar',
    redirect_uri:'http://localhost/auth/google_oauth2/callback'
  }
end

