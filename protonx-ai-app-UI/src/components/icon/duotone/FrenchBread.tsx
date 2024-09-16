import React, { SVGProps } from 'react';

const SvgFrenchBread = (props: SVGProps<SVGSVGElement>) => {
	return (
		<svg viewBox='0 0 24 24' className='svg-icon' {...props}>
			<g fill='none' fillRule='evenodd'>
				<path d='M0 0h24v24H0z' />
				<path
					d='M11.195 6.192c.1.074.213.13.34.164l3.268.876a1 1 0 00.518-1.932l-2.093-.56c3.267-2.078 6.26-2.723 7.61-1.372 1.953 1.953-.263 7.335-4.949 12.021-4.686 4.686-10.068 6.902-12.02 4.95-1.244-1.243-.798-3.875.9-6.833.02.008.043.015.065.02l2.898.777a1 1 0 10.518-1.932l-2.347-.628c.472-.662.999-1.33 1.576-1.992l.054.016 3.735 1a1 1 0 00.517-1.931L9.04 8.1a27.943 27.943 0 012.156-1.908z'
					fill='currentColor'
				/>
			</g>
		</svg>
	);
};

export default SvgFrenchBread;
