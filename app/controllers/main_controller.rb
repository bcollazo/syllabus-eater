class MainController < ApplicationController

	def index
	end

	def upload
		ip_address = request.remote_ip

		syllabi = ["1", "2", "3", "4", "5"]
		syllabi.each do |s|
			uploaded_io = params[s]
			if uploaded_io == nil
				next
			end
			path = File.dirname(Rails.root.join("public/uploads", ip_address.to_s, uploaded_io.original_filename))
			puts = "path = "+path
			unless File.directory?(path)
				FileUtils.mkdir_p(path)
			end
			File.open(Rails.root.join('public/uploads', ip_address, uploaded_io.original_filename), 'wb') do |file|
				file.write(uploaded_io.read)
			end
		end
		redirect_to dashboard_url
	end

	def dashboard
		@classes = ["Theory de Computacion","Mathematics for Men", "Machine Learning"]
		@information = {"Theory de Computacion"=>{"code"=>["1.111", 0], "prof_name"=>["Sadoway", 0], "email"=>["sadoway@mit.edu", 0], "phone"=>["111-111-1111", 0], "meeting_times"=>["Google calendar quick add magic", 0], "location"=>["10-250", 0], "important_dates"=>["More black magic papi", 0], "grading_scheme"=>["Not enough vespene gas", 0], "website"=>["www.mit.edu",0], "calendar"=>["97govrrrbtgthvpq8q1s4r4p5c",0]}, "Mathematics for Men"=>{"code"=>["1.112", 0], "prof_name"=>["Kelner", 0], "email"=>["kelner@mit.edu", 0], "phone"=>["222-222-2222", 0], "meeting_times"=>["Google calendar quick add magic", 0], "location"=>["Walker", 0], "important_dates"=>["More black magic papi", 0], "grading_scheme"=>["Not enough vespene gas", 0], "website"=>["www.mit.edu",0], "calendar"=>["97govrrrbtgthvpq8q1s4r4p5c",0]}, "Machine Learning"=>{"code"=>["1.113", 0], "prof_name"=>["Jaakola", 0], "email"=>["jaakola@mit.edu", 0],"phone"=>["333-333-3333", 0], "meeting_times"=>["Google calendar quick add magic", 0], "location"=>["54-100", 0], "important_dates"=>["More black magic papi", 0],"grading_scheme"=>["Not enough vespene gas", 0], "website"=>["www.mit.edu",0], "calendar"=>["97govrrrbtgthvpq8q1s4r4p5c",0]}}
	end

	def processSyllabus
		ip_address = request.remote_ip
		command = "python script/2textconv/2txtconvert.py "+ip_address+" 2>&1"
		value = system(command)

		command ='python script/example.py '+ip_address+' 2>&1'
		kidoutput = `python script/example.py `+ip_address+` 2>&1`
		puts kidoutput
	end

	def about
	end

	def create     
		#What data comes back from OmniAuth?     
		@auth = request.env["omniauth.auth"]
		#Use the token from the data to request a list of calendars
		@token = @auth["credentials"]["token"]
		client = Google::APIClient.new
		client.authorization.access_token = @token
		service = client.discovered_api('calendar', 'v3')
		@result = client.execute(
		  :api_method => service.calendar_list.list,
		  :parameters => {},
		  :headers => {'Content-Type' => 'application/json'})
		puts @result
	end

end
