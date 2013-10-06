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
		ip_address = request.remote_ip

		value = %x('python scripts/2textconv/2totextconverter.py '+ip_address+ ' 2>&1')

		#kidoutput = %x('python alchemy.py 2>&1')

		@classes = ["18.404 Theory","Mathematics for Men"]
	end

	def about
	end

end
