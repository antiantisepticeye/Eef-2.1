from __future__ import annotations
import os
import io, aiohttp, numpy as np, cv2
from PIL import Image
from .kromo import add_chromatic
from .legofy import legofy_image

def overlay(image1, image2):
	print(image2)
	r, g, b, a = cv2.split(image2)
	return a

	
ASSET_DIRECTORY = "./src/extensions/image/assets/"
ASSET_IMAGES = {
	"wasted": cv2.imread(ASSET_DIRECTORY + "wasted.png", cv2.IMREAD_UNCHANGED),
	"wanted": cv2.imread(ASSET_DIRECTORY + "wanted.png", cv2.IMREAD_UNCHANGED),
}	

class cv_Image:
	
	ASSET_DIRECTORY = ASSET_DIRECTORY
	legofy_brick_image = Image.open(ASSET_DIRECTORY + "legofy.png")

	def __init__(self, image: np.ndarray) -> None:
		self.data = image
	
	@staticmethod
	async def from_url(url: str) -> cv_Image:
		async with aiohttp.ClientSession() as session:
			async with session.get(url) as resp:
				d = await resp.read()
				image = np.asarray(bytearray(d), dtype="uint8")
				image = cv2.imdecode(image, cv2.IMREAD_COLOR)
				return cv_Image(image)
	
	@staticmethod
	def from_asset(asset_name: str) -> cv_Image:
		return cv_Image(ASSET_IMAGES[asset_name])

	@staticmethod
	def overlay(base: cv_Image, over: cv_Image, alpha: float=None) -> cv_Image:
		over = over.resize(base.data.shape[0], base.data.shape[1])
		if alpha == None:
			c = cv2.split(over.data)
			if len(c) > 3: 
				a = cv2.cvtColor(c[3], cv2.COLOR_GRAY2BGR) / 255
			else: a = 1
		else:
			c = cv2.split(over.data)
			a = float(alpha)
		over.data = cv2.cvtColor(over.data, cv2.COLOR_BGRA2BGR)
		data = base.data * (1-a) + over.data * a
		return cv_Image(data)
	
	@staticmethod
	def chromatic(image: cv_Image, strength: float=1.5, no_blur:bool=False) -> cv_Image:
		d = image.data
		
		width = d.shape[1]
		height = d.shape[0]
		
		if (width % 2 == 0):
			d = d[:, :-1, :]
		
		if (height % 2 == 0):
			d = d[:-1, :, :]
		
		image = add_chromatic(Image.fromarray(d, "RGB"), strength, no_blur)
		
		return cv_Image(np.asarray(image, dtype="uint8"))
	
	@staticmethod
	def legofy(image: cv_Image) -> cv_Image:
		src = Image.fromarray(image.data)
		brick = cv_Image.legofy_brick_image
		out = legofy_image(src, brick, None, None, None, False)
		return cv_Image(np.asarray(out, dtype="uint8"))

	def channels(self):
		return cv2.split(self.data)
	
	def channels_len(self) -> int:
		return self.data.shape[2] or 1
	
	def to_buffer(self) -> bytes:
		success, data = cv2.imencode('.png', self.data)
		buffer = io.BytesIO(data.tobytes())
		return buffer
	
	def resize(self, x_dim: int, y_dim: int) -> cv_Image:
		dsize = (x_dim, y_dim)
		out = cv2.resize(self.data, dsize)
		self.data = out
		return self

	def greyscale(self) -> cv_Image:
		if self.channels_len() == 3:
			self.data = cv2.cvtColor(cv2.cvtColor(self.data, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR) 
		else:
			self.data = cv2.cvtColor(cv2.cvtColor(self.data, cv2.COLOR_BGRA2GRAY), cv2.COLOR_GRAY2BGRA)
		return self
	
	def paste(self, src: cv_Image, x_off:int=0, y_off:int=0, filter_:str="normal") -> cv_Image:
		base = cv2.cvtColor(self.data, cv2.COLOR_BGR2BGRA)
		src = cv2.cvtColor(src.data, cv2.COLOR_BGR2BGRA)
		if len(src.shape) > 3:
			a = cv2.cvtColor(cv2.split(src)[3], cv2.COLOR_GRAY2BGRA) / 255
		else:
			a = 1
		x_end = x_off + src.shape[1]
		y_end = y_off + src.shape[0]
		
		d = base[y_off:y_end, x_off:x_end]
		if filter_ == "normal":
			d = d * (1-a) + (src * a)

		elif filter_ == "multiply":
			d = (d/255) * (src/255) * 255
		
		base[y_off:y_end, x_off:x_end] = d
		
		self.data = base
		return self
	
