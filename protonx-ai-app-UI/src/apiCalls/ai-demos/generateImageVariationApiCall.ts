import axios from 'axios';
import { AI_DEMOS_URI, HOST } from '@/constant';

export function generateImageVariationApiCall(data: {
	dataToPost: {
		base64: string;
	};
}) {
	const { dataToPost } = data;
	return axios({
		method: 'post',
		url: `https://2ed4-34-168-140-68.ngrok-free.app/sam2`,
		data: dataToPost,
	});
}
