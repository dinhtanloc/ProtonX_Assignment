import React, { SVGProps } from 'react';

const SvgFont = (props: SVGProps<SVGSVGElement>) => {
	return (
		<svg viewBox='0 0 24 24' className='svg-icon' {...props}>
			<g fill='none' fillRule='evenodd'>
				<path d='M0 0h24v24H0z' />
				<path
					d='M.18 19L7.1 4.64 14.02 19h-1.96l-1.76-3.72H3.9L2.14 19H.18zM7.1 8.52L4.7 13.6h4.8L7.1 8.52z'
					fill='currentColor'
				/>
				<path
					d='M21.34 19v-1c-.84.76-1.96 1.16-3.18 1.16-2.94 0-5.1-2.26-5.1-5.16 0-2.9 2.16-5.16 5.1-5.16 1.22 0 2.34.4 3.18 1.16V9h1.72v10h-1.72zm-3.14-1.46c1.44 0 2.56-.68 3.14-1.62v-3.84c-.58-.94-1.7-1.62-3.14-1.62-1.96 0-3.36 1.56-3.36 3.54s1.4 3.54 3.36 3.54z'
					fill='currentColor'
					opacity={0.3}
				/>
			</g>
		</svg>
	);
};

export default SvgFont;
